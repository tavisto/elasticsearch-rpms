#!/usr/bin/env python
""" Grabs all the sources for a given version number of elasticsearch """

import urlgrabber
from optparse import OptionParser


parser = OptionParser()
(options,args) = parser.parse_args()
print "Getting Main Source for version %s " % args[0]
urlgrabber.urlgrab('https://github.com/downloads/elasticsearch/elasticsearch/elasticsearch-%s.tar.gz' % args[0])
print "Getting plugin-lang-python"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/lang-python/elasticsearch-lang-python-%s.zip' % args[0])
print "Getting plugin-lang-javascript"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/lang-javascript/elasticsearch-lang-javascript-%s.zip' % args[0])
print "Getting plugin-lang-groovy"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/lang-groovy/elasticsearch-lang-groovy-%s.zip' % args[0])
print "Getting plugin-river-couchdb"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/river-couchdb/elasticsearch-river-couchdb-%s.zip' % args[0])
print "Getting plugin-river-rabbitmq"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/river-rabbitmq/elasticsearch-river-rabbitmq-%s.zip' % args[0])
print "Getting plugin-river-twitter"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/river-twitter/elasticsearch-river-twitter-%s.zip' % args[0])
print "Getting plugin-river-wikipedia"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/river-wikipedia/elasticsearch-river-wikipedia-%s.zip' % args[0])