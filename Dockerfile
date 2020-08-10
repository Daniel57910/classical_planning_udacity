FROM pypy:3
WORKDIR /usr/src/app
COPY . .
RUN ls
RUN pip install pandas
CMD ["pypy3", "/usr/src/app/run_search.py", "-p 1 2 -s 1 2 3 4 5 6 7 8 9 10 11" ]




