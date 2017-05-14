#!/bin/sh
scriptdir=`dirname $0`

java -mx700m -cp "$scriptdir/stanford-parser.jar:$scriptdir/lib/*" edu.stanford.nlp.process.DocumentPreprocessor $1
