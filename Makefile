sync:
	git push origin main

image:
	sudo mkosi build

serve:
	# /hugo/hugo serve
	/hugo/hugo server --bind 0.0.0.0 --port 9333

build:
	/hugo/hugo --ignoreCache=true --minify
