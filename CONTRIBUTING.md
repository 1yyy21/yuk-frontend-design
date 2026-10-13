# Contributing

Small, evidence-backed improvements are welcome: resource links, compatibility guidance, routing corrections, and reproducible integration examples.

1. Describe the frontend task and the problem your change solves.
2. Keep the skill independent of your machine, credentials, and private project details.
3. For a new source, include its official URL, intended use, integration method, and where licensing must be checked. Update the documented source count if it changes.
4. Do not include copied third-party component code without its required license and attribution. Never commit tokens, `.env` files, browser profiles, or private logs.
5. Run `python scripts/validate.py` after installing `requirements-dev.txt`.
6. In the pull request, distinguish static validation from an actual agent/browser trial. Describe the trial if one was run.

The skill should retain the user's existing stack and permissions. Do not add instructions that claim blanket authority to install, publish, buy, or deploy.

中文：欢迎提交有依据的小改进。提供具体场景、官方来源、适配方法和验证证据；避免上传个人配置、密钥及未经授权的素材。
