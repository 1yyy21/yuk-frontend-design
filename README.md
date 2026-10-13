# yuk-frontend-design — Frontend Design & UI Component Discovery

**Find the right UI. Integrate it into your project. Verify the result.**

[中文](README.zh-CN.md) · [Skill instructions](skills/yuk-frontend-design/SKILL.md) · [24 sources](skills/yuk-frontend-design/references/sources.md) · [MIT](LICENSE)

An agent skill for frontend development that searches a curated library of **24 design resources**, selects components and motion that fit your stack, and integrates the selected implementation into the actual interface.

Use it for **frontend design**, **UI/UX polish**, **UI component discovery**, **CSS animations**, **React components**, **Tailwind CSS integration**, **web design inspiration**, icons, and typography. It is packaged as an **Agent Skill** for coding agents such as Codex; agents such as Claude Code and Cursor can use the same `SKILL.md` format through their supported installation workflows.

It connects design discovery to working code: identify the project → search relevant sources → check compatibility and licensing → install or adapt → verify the page.

## Install

**v0.2.0 integrated edition:** one entry point combines resource discovery, offline design search, component contracts, and page verification. Selected MIT / Apache-2.0 upstream materials are pinned and attributed. See [integration details](skills/yuk-frontend-design/references/integrations.md).

Using the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add 1yyy21/yuk-frontend-design --skill yuk-frontend-design
```

For a global Codex installation:

```bash
npx skills add 1yyy21/yuk-frontend-design --skill yuk-frontend-design --agent codex --global
```

Alternatively, clone this repository and copy `skills/yuk-frontend-design` to your agent's skill directory. For Codex, use `$CODEX_HOME/skills`, or `~/.codex/skills` if `CODEX_HOME` is unset. Other agents have their own discovery rules; check their documentation.

## Use

In Codex, invoke explicitly with `$yuk-frontend-design`, or let the agent select it for relevant frontend tasks when implicit invocation is supported.

```text
Use $yuk-frontend-design to polish this React settings page.
Find suitable switches, cards, and subtle animations,
integrate them with the existing styles, and verify mobile behavior.
```

```text
Use $yuk-frontend-design to add a CSS loading animation to this plain HTML page.
Keep the current structure and avoid introducing a framework.
```

```text
Use $yuk-frontend-design to prepare a separate preview of a new dashboard style.
Show the preview before changing the production source.
```

## What it does

| Stage | Behavior |
| --- | --- |
| Understand | Reads project conventions, stack, dependencies, and existing components |
| Discover | Searches a focused subset of relevant official resource pages |
| Select | Checks visual fit, compatibility, dependency cost, and reuse permission |
| Integrate | Installs selected dependencies or adapts reusable source within user authorization |
| Verify | Runs relevant checks and inspects actual interactions and responsive layouts |
| Record | Records sources, versions, license evidence, and validation in the project |

**Resources include:** Uiverse, 21st.dev, React Bits, Magic UI, Animata, Aceternity UI, Codrops, CodePen, three.js, Norrly, MotionSites, SVG Repo, LottieFiles, and font resources. The [catalog](skills/yuk-frontend-design/references/sources.md) contains all 24 entries and routing guidance.

## Discover this category

In the [Skills directory](https://skills.sh/), start with these task-specific search terms:

| Looking for | Search terms |
| --- | --- |
| Interface design and polish | `frontend-design`, `ui-ux`, `web-design` |
| Resource discovery and integration | `design-resources`, `design-resource-library`, `ui-components`, `component-library` |
| UI motion and reusable effects | `css-animation`, `react-bits`, `magic-ui`, `aceternity-ui`, `uiverse` |
| Agent-specific skills | `agent-skills`, `codex-skills`, `claude-code-skills` |

```bash
npx skills find frontend-design
npx skills find design-resources
npx skills find ui-components
npx skills find react-bits
```

For GitHub repository search, try `topic:agent-skills frontend`, `topic:frontend-design skill`, or `"design-resource-library"`. To find this project directly, search `yuk-frontend-design` or use its installation command above. A new GitHub repository may take time to appear in search and third-party directories; these keywords do not guarantee ranking or directory inclusion.

## Requirements and boundaries

- An agent that can load `SKILL.md`, access the web, and edit your project. Dependency installation also requires command execution and the project's package manager.
- This is an agent skill with an offline design search tool, not a background service or UI asset library. It does not install all 24 libraries. Python 3.10+ is required only for offline search.
- Existing project components take priority when suitable. React examples are not inserted into unrelated frameworks without adaptation.
- User permissions and project rules apply. Paid downloads, production deployment, and external publication require their own authorization.
- Third-party components, fonts, and media keep their own licenses. The MIT license covers this repository's original instructions and tooling.
- Browser validation depends on tools available in the host agent. Missing visual validation must be reported rather than assumed.

The primary instructions are Chinese; this README provides an English overview. Included: Design Resource Library's reference, UI UX Pro Max's search engine and datasets, Impeccable's craft floor, and original component integration guidance with an optional Component Gallery Skill route. Full upstream runtimes and hooks are not included.

```bash
python skills/yuk-frontend-design/scripts/design-search.py "keyboard focus" --domain ux --json
python skills/yuk-frontend-design/scripts/design-search.py "form validation" --stack react --json
```

## Repository structure

```text
skills/yuk-frontend-design/
  SKILL.md                 Agent instructions
  agents/openai.yaml       Codex UI metadata and implicit invocation policy
  references/sources.md    Curated resource catalog
scripts/validate.py        Repository validation
.github/workflows/         Continuous validation
```

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). To validate a change:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

## Acknowledgments

Repository organization and installation conventions were informed by [anthropics/skills](https://github.com/anthropics/skills), [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), and the [Agent Skills format](https://agentskills.io/). This is an independent project; it does not imply endorsement by those maintainers or by the resource sites.

## License

[MIT](LICENSE) for original yuk-frontend-design work; vendored files retain MIT or Apache-2.0. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
