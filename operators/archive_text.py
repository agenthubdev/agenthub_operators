import re

from .base_operator import BaseOperator

from ai_context import AiContext


class ArchiveText(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Archive Text'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.DB.value
    
    @staticmethod    
    def declare_parameters():
        return [
            {
                "name": "table_name",
                "data_type": "string",
                "placeholder": "Table name to store in"
            },
            {
                "name": "visibility",
                "data_type": "enum(team,user,public)",
                "description": "*visibility=user* means that everybody who runs the pipeline/agent would store in their own private database table and nobody else could access it. *visibility=team* is same as user level but for the team, i.e. table is visible only to the team members. *visibility=public* will write to table that everybody can access."
            },
            {
                "name": "team_name",
                "data_type": "string",
                "placeholder": "Team name that will have access to subject table",
                "condition": "visibility == team"
            },
            {
                "name": "split_by",
                "data_type": "enum(line,chunk)",
            },
            {
                "name": "chunk_size_words",
                "data_type": "string",
                "placeholder": "Desired word count in each chunk",
                "condition": "split_by == chunk"
            },
            {
                "name": "language",
                "data_type": "enum(english,simple,arabic,armenian,basque,catalan,danish,dutch,finnish,french,german,greek,hindi,hungarian,indonesian,irish,italian,lithuanian,nepali,norwegian,portuguese,romanian,russian,serbian,spanish,swedish,tamil,turkish,yiddish)"
            },
            {
                "name": "overwrite",
                "data_type": "boolean"
            }
        ]
    
    @staticmethod    
    def declare_inputs():
        return [
            {
                "name": "text",
                "data_type": "string",
            }
        ]
    
    @staticmethod    
    def declare_outputs():
        return [
        ]

    def run_step(
        self,
        step,
        ai_context: AiContext
    ):
        p = step['parameters']
        text = ai_context.get_input('text', self)
        if p['split_by'] == 'line':
            chunks = text.splitlines()
        elif p['split_by'] == 'chunk':
            chunks = ArchiveText.split_text_into_chunks(text, p['chunk_size_words'])
        else:
            raise ValueError(f"Don't know what to do with value {p['split_by']} of parameter 'split_by'")
        
        ai_context.index_chunks(
            chunks, 
            table_name=p['table_name'],
            visibility=p['visibility'],
            team_name=p.get('team_name'),
            language=p.get('language', 'english'),
            overwrite=p.get('overwrite', False)
        )
        

    @staticmethod
    def split_text_into_chunks(text, target_word_count):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks = []
        first_sentence_index = 0
        current_word_count = 0
        for last_sentence_index, sentence in enumerate(sentences):
            sentence_word_count = len(sentence.split())
            new_word_count = current_word_count + sentence_word_count

            if current_word_count >= (target_word_count - 5):
                # Chunk without last_sentence_index is a eligible to be formed.
                if abs(current_word_count - target_word_count) < abs(new_word_count - target_word_count):
                    # Adding last_sentence_index to the chunk would make it worse.
                    chunks.append(" ".join(sentences[first_sentence_index:last_sentence_index]).strip())
                    first_sentence_index = last_sentence_index
                    current_word_count = sentence_word_count
                    continue
            
            # If new chunk was not formed then last_sentence_index should be a part of current pending chunk candidate.
            current_word_count = new_word_count
            
        # Add the last chunk
        if first_sentence_index < len(sentences):
            chunks.append(" ".join(sentences[first_sentence_index:]).strip())
        return chunks
        
        
    
   
