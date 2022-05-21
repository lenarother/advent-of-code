help:
	@echo "day - generate template files for day challenge"
	@echo "clean - clean pyc files and so on"
	@echo "readme - generate README.rst"
	@echo "stat - show AoC statistic"
	@echo "test - run tests"

clean:
	rm -rf adventofcode_*/.pytest_cache
	rm -rf adventofcode_*/day_*/.pytest_cache
	find . -name \*.pyc -delete

day:
	python template/make_day.py

readme:
	python resources/src/make_readme.py

stat:
	python resources/src/make_stats.py

test:
	pytest --flake8 --isort
