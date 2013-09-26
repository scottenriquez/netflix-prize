all:
	make Netflix.zip

clean:
	rm -f Netflix.html
	rm -f Netflix.log
	rm -f Netflix.zip
	rm -f RunNetflix.out
	rm -f RunNetflix.tmp
	rm -f TestNetflix.out
	rm -f *.pyc

diff: RunNetflix.in RunNetflix.out RunNetflix.py
	RunNetflix.py < RunNetflix.in > RunNetflix.tmp
	diff RunNetflix.out RunNetflix.tmp
	rm RunNetflix.tmp

turnin-list:
	turnin --list thunt cs373pj2

turnin-submit: Netflix.zip
	turnin --submit thunt cs373pj2 Netflix.zip

turnin-verify:
	turnin --verify thunt cs373pj2

Netflix.html: Netflix.py
	pydoc -w Netflix

Netflix.log:
	git log > Netflix.log

Netflix.zip: makefile                                   \
             Netflix.html Netflix.log Netflix.py        \
             RunNetflix.in RunNetflix.out RunNetflix.py \
             TestNetflix.py TestNetflix.out
	zip -r Netflix.zip                                \
	       makefile                                   \
           Netflix.html Netflix.log Netflix.py        \
           RunNetflix.in RunNetflix.out RunNetflix.py \
           TestNetflix.py TestNetflix.out

RunNetflix.out: RunNetflix.in RunNetflix.py
	RunNetflix.py < RunNetflix.in > RunNetflix.out

TestNetflix.out: TestNetflix.py
	TestNetflix.py > TestNetflix.out
