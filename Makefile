install: #установка завсисмостей
	uv sync

build: #билд проекта. Существуют и другие каталоги, да и даже репозитории как Github или Gitlab позволяют публиковать установочные пакеты
	uv build

package-install: #установить пакет в операционную систему
	uv tool install dist/*.whl

brain-games: #запуск проекта
	uv run brain-games

lint:
	uv run ruff check brain_games


