help:
	@echo "day - generate template files for day challenge"
	@echo "clean - clean pyc files and so on"

clean:
	rm -rf adventofcode_*/.pytest_cache
	rm -rf adventofcode_*/day_*/.pytest_cache
	find . -name \*.pyc -delete

day:
	python template/make_day.py
