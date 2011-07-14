#!/usr/bin/env python
""" Grabs all the sources for a given version number of elasticsearch """

import urlgrabber
from optparse import OptionParser


parser = OptionParser()
(options,args) = parser.parse_args()
print "Getting Main Source for version %s " % args[0]
urlgrabber.urlgrab('https://github.com/downloads/elasticsearch/elasticsearch/elasticsearch-%s.tar.gz' % args[0])
print "Getting plugin-analysis-icu"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/analysis-icu/elasticsearch-analysis-icu-%s.zip' % args[0])
print "Getting plugin-cloud-aws"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/cloud-aws/elasticsearch-cloud-aws-%s.zip' % args[0])
print "Getting plugin-hadoop"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/hadoop/elasticsearch-hadoop-%s.zip' % args[0])
print "Getting plugin-lang-groovy"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/lang-groovy/elasticsearch-lang-groovy-%s.zip' % args[0])
print "Getting plugin-lang-javascript"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/lang-javascript/elasticsearch-lang-javascript-%s.zip' % args[0])
print "Getting plugin-lang-python"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/lang-python/elasticsearch-lang-python-%s.zip' % args[0])
print "Getting plugin-mapper-attachments"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/mapper-attachments/elasticsearch-mapper-attachments-%s.zip' % args[0])
print "Getting plugin-river-couchdb"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/river-couchdb/elasticsearch-river-couchdb-%s.zip' % args[0])
print "Getting plugin-river-rabbitmq"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/river-rabbitmq/elasticsearch-river-rabbitmq-%s.zip' % args[0])
print "Getting plugin-river-twitter"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/river-twitter/elasticsearch-river-twitter-%s.zip' % args[0])
print "Getting plugin-river-wikipedia"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/river-wikipedia/elasticsearch-river-wikipedia-%s.zip' % args[0])
print "Getting plugin-transport-memcached"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/transport-memcached/elasticsearch-transport-memcached-%s.zip' % args[0])
print "Getting plugin-transport-thrift"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/transport-thrift/elasticsearch-transport-thrift-%s.zip' % args[0])
print "Getting plugin-transport-wares"
urlgrabber.urlgrab('http://elasticsearch.googlecode.com/svn/plugins/transport-wares/elasticsearch-transport-wares-%s.zip' % args[0])
