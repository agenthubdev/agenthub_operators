<p align="center">
<br><br>
<a "https://agenthub.dev/"><img src="https://cdn.discordapp.com/attachments/1121495367444332605/1121495431545880586/robot_1f916.png" width="150px"></a>
</p>

<div align="center">
  <h3><strong>AgentHub</strong></h3>
</div>


<p align=center>
<a href="https://github.com/misha-agenthub/agenthub_operators/graphs/commit-activity"><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg"></a>
<a href="https://github.com/misha-agenthub/agenthub_operators/blob/master/LICENSE"><img src="https://img.shields.io/github/license/misha-agenthub/agenthub_operators"></a>
<a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"></a>
<a href="https://discord.gg/nVrtEJryA4"><img src="https://dcbadge.vercel.app/api/server/nVrtEJryA4?compact=true&style=flat"></a>
</p>

<p align="center">
<b><em>Build and Host AI powered pipelines</em></b>
</p>


<!-- <p align="center">
<a href="https://github.com/misha-agenthub/agenthub_operators/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=misha-agenthub/agenthub_operators" />
</a> -->

# About

This repository contains all public AgentHub operators [agenthub.dev](https://agenthub.dev). AgentHub as a platform hosts and runs your AI pipelines that are built with these open source operators. 

# What is an Operator

Each AI powered pipeline on AgentHub is made up of modular components called operators. An operator is a small building block that performs an explicit action (Ex: GmailReader reads emails, AskChatGPT queries the openAI api, Tweet send a tweet).

Each operator is a short python script wrapped in the same rigid structure that definines inputs, parameters, outputs and the "run_step". The run_step contains the logic of each operator. 

If AgentHub is ever missing an operator you need it's only a few lines of python away from existing. Message in the discord for help creating it or raise a PR to add your own custom operator. 

## Documentation

All operators in this repository are thoroughly documented in the `/docs` folder. What makes our documentation truly unique is that it is completely generated using GPT-4 via an AgentHub automation. We run this automation regularly ensuring it is always up-to-date and in sync with the current state of the project.

To access the operator documentation, navigate to the `/docs` directory, or you can view it online [here](https://github.com/agenthubdev/agenthub_operators/tree/main/docs).

## Contributing

We warmly welcome contributions! If you've devised a new operator and want to share it with the community, feel free to submit a pull request.

## Community

For those of you who need assistance, wish to discuss ideas, or just want to be part of the developer community, join us on Discord! Here's our [Discord invite link](https://discord.gg/SyCVmrzhCc).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=agenthubdev/agenthub_operators&type=Date)](https://star-history.com/#agenthubdev/agenthub_operators&Date)
