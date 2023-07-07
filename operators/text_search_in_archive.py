import re

from .base_operator import BaseOperator

from ai_context import AiContext


class TextSearchInArchive(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Text Search in Archive'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.DB.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "query",
                "data_type": "string",
                "placeholder": "Query to search for (can be an input instead of parameter)"
            },
            {
                "name": "num_results",
                "data_type": "string",
                "placeholder": "Limit on number of results to return (optional, default=10)"
            },
            {
                "name": "table_name",
                "data_type": "string",
                "placeholder": "Table name to search in"
            },
            {
                "name": "visibility",
                "data_type": "enum(project,user,public)",
            },
            {
                "name": "language",
                "data_type": "enum(english,simple,arabic,armenian,basque,catalan,danish,dutch,finnish,french,german,greek,hindi,hungarian,indonesian,irish,italian,lithuanian,nepali,norwegian,portuguese,romanian,russian,serbian,spanish,swedish,tamil,turkish,yiddish)"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "query",
                "data_type": "string",
                "optional": "1",
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "search_results",
                "data_type": "string",
            }
        ]

    def run_step(
        self,
        step,
        ai_context: AiContext
    ):
        p = step['parameters']
        query = ai_context.get_input('query', self) or p['query']

        r = ai_context.query_chunk_index(
            query,
            p.get('num_results', 10),
            p['table_name'],
            p['visibility'],
            p.get('language', 'english'),
        )

        ai_context.set_output('search_results', str(r), self)
        ai_context.add_to_log(f'Found: {r}')
