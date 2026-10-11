name: Gerar cobrinha das contribuições

on:
  schedule:
    - cron: "0 */12 * * *"   # atualiza sozinha a cada 12 horas
  workflow_dispatch:          # permite rodar manualmente pela aba Actions
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - name: Gerar SVG da cobrinha em tons de roxo
        uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-snake.svg
            dist/github-snake-dark.svg?palette=github-dark&color_snake=#C084FC&color_dots=#161b22,#3b2a6b,#5b3fa0,#8b5cf6,#c084fc

      - name: Publicar na branch output
        uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
