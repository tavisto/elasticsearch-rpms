%define debug_package %{nil}

Name:           elasticsearch
Version:        0.18.5
Release:        1%{?dist}
Summary:        A distributed, highly available, RESTful search engine

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            http://www.elasticsearch.com
Source0:        https://github.com/downloads/%{name}/%{name}/%{name}-%{version}.tar.gz
Source1:        init.d-elasticsearch
Source2:        logrotate.d-elasticsearch
Source3:        config-logging.yml
Source4:        sysconfig-elasticsearch
Source5:        http://elasticsearch.googlecode.com/svn/plugins/analysis-icu/elasticsearch-analysis-icu-%{version}.zip
Source6:        http://elasticsearch.googlecode.com/svn/plugins/cloud-aws/elasticsearch-cloud-aws-%{version}.zip
Source7:        http://elasticsearch.googlecode.com/svn/plugins/hadoop/elasticsearch-hadoop-%{version}.zip
Source8:        http://elasticsearch.googlecode.com/svn/plugins/lang-groovy/elasticsearch-lang-groovy-%{version}.zip
Source9:        http://elasticsearch.googlecode.com/svn/plugins/lang-javascript/elasticsearch-lang-javascript-%{version}.zip
Source10:       http://elasticsearch.googlecode.com/svn/plugins/lang-python/elasticsearch-lang-python-%{version}.zip
Source11:       http://elasticsearch.googlecode.com/svn/plugins/mapper-attachments/elasticsearch-mapper-attachments-%{version}.zip
Source12:       http://elasticsearch.googlecode.com/svn/plugins/river-couchdb/elasticsearch-river-couchdb-%{version}.zip
Source13:       http://elasticsearch.googlecode.com/svn/plugins/river-rabbitmq/elasticsearch-river-rabbitmq-%{version}.zip
Source14:       http://elasticsearch.googlecode.com/svn/plugins/river-twitter/elasticsearch-river-twitter-%{version}.zip
Source15:       http://elasticsearch.googlecode.com/svn/plugins/river-wikipedia/elasticsearch-river-wikipedia-%{version}.zip
Source16:       http://elasticsearch.googlecode.com/svn/plugins/transport-memcached/elasticsearch-transport-memcached-%{version}.zip
Source17:       http://elasticsearch.googlecode.com/svn/plugins/transport-thrift/elasticsearch-transport-thrift-%{version}.zip
Source18:       http://elasticsearch.googlecode.com/svn/plugins/transport-wares/elasticsearch-transport-wares-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       jpackage-utils
Requires:       java

Requires(post): chkconfig initscripts
Requires(pre):  chkconfig initscripts
Requires(pre):  shadow-utils

%description
A distributed, highly available, RESTful search engine

%package plugin-analysis-icu
BuildArch:      noarch
Summary:        An analysis plugin to add support for ICU
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-analysis-icu
A analysis plugin to add support for ICU

%package plugin-cloud-aws
BuildArch:      noarch
Summary:        A discovery plugin to add support for EC2
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-cloud-aws
A discovery plugin to add support for EC2

%package plugin-hadoop
BuildArch:      noarch
Summary:        A gateway to store cluster meta and indices data in Hadoop
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-hadoop
A gateway to store cluster meta and indices data in Hadoop

%package plugin-lang-groovy
BuildArch:      noarch
Summary:        A lang plugin to add support for Groovy
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-lang-groovy
A lang plugin to add support for Groovy

%package plugin-lang-javascript
BuildArch:      noarch
Summary:        A lang plugin to add support for JavaScript
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-lang-javascript
A lang plugin to add support for JavaScript

%package plugin-lang-python
BuildArch:      noarch
Summary:        A lang plugin to add support for Python
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-lang-python
A lang plugin to add support for Python

%package plugin-mapper-attachments
BuildArch:      noarch
Summary:        Adds the attachment type allowing to parse difference attachment formats
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-mapper-attachments
Adds the attachment type allowing to parse difference attachment formats

%package plugin-river-couchdb
BuildArch:      noarch
Summary:        A river plugin to index from a couchdb database
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-river-couchdb
The CouchDB River allows to automatically index couchdb and make it searchable using the excellent _changes stream couchdb provides

%package plugin-river-rabbitmq
BuildArch:      noarch
Summary:        A river plugin to index from a rabbitmq queue
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-river-rabbitmq
RabbitMQ River allows to automatically index a rabbitmq queue

%package plugin-river-twitter
BuildArch:      noarch
Summary:        A river plugin to index from a twitter feed
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-river-twitter
The twitter river indexes the public twitter stream, aka the hose, and makes it searchable

%package plugin-river-wikipedia
BuildArch:      noarch
Summary:        A river plugin to index wikipedia
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-river-wikipedia
A simple river to index wikipedia

%package plugin-transport-memcached
BuildArch:      noarch
Summary:        Exports elasticsearch APIs over memcached
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-transport-memcached
Exports elasticsearch APIs over memcached

%package plugin-transport-thrift
BuildArch:      noarch
Summary:        Exports elasticsearch APIs over thrift
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-transport-thrift
Exports elasticsearch APIs over thrift

%package plugin-transport-wares
BuildArch:      noarch
Summary:        Servlet that can be used to dispatch requests to elasticsearch
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-transport-wares
Servlet that can be used to dispatch requests to elasticsearch



%prep
%setup -q -n %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE5} -d plugins/analysis-icu
unzip %{SOURCE6} -d plugins/cloud-aws
unzip %{SOURCE7} -d plugins/hadoop
unzip %{SOURCE8} -d plugins/lang-groovy
unzip %{SOURCE9} -d plugins/lang-javascript
unzip %{SOURCE10} -d plugins/lang-python
unzip %{SOURCE11} -d plugins/mapper-attachments
unzip %{SOURCE12} -d plugins/river-couchdb
unzip %{SOURCE13} -d plugins/river-rabbitmq
unzip %{SOURCE14} -d plugins/river-twitter
unzip %{SOURCE15} -d plugins/river-wikipedia
unzip %{SOURCE16} -d plugins/transport-memcached
unzip %{SOURCE17} -d plugins/transport-thrift
unzip %{SOURCE18} -d plugins/transport-wares

%build
true

%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}%{_javadir}/%{name}/bin
%{__install} -p -m 755 bin/elasticsearch %{buildroot}%{_javadir}/%{name}/bin
%{__install} -p -m 644 bin/elasticsearch.in.sh %{buildroot}%{_javadir}/%{name}/bin
%{__install} -p -m 755 bin/plugin %{buildroot}%{_javadir}/%{name}/bin

#libs
%{__mkdir} -p %{buildroot}%{_javadir}/%{name}/lib/sigar
%{__install} -p -m 644 lib/*.jar %{buildroot}%{_javadir}/%{name}/lib
%{__install} -p -m 644 lib/sigar/*.jar %{buildroot}%{_javadir}/%{name}/lib/sigar
%ifarch i386
%{__install} -p -m 644 lib/sigar/libsigar-x86-linux.so %{buildroot}%{_javadir}/%{name}/lib/sigar
%endif
%ifarch x86_64
%{__install} -p -m 644 lib/sigar/libsigar-amd64-linux.so %{buildroot}%{_javadir}/%{name}/lib/sigar
%endif

# config
%{__mkdir} -p %{buildroot}%{_sysconfdir}/elasticsearch
%{__install} -m 644 config/elasticsearch.yml %{buildroot}%{_sysconfdir}/%{name}
%{__install} -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/logging.yml

# data
%{__mkdir} -p %{buildroot}%{_localstatedir}/lib/%{name}

# logs
%{__mkdir} -p %{buildroot}%{_localstatedir}/log/%{name}
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/elasticsearch

# plugins
%{__mkdir} -p %{buildroot}%{_javadir}/%{name}/plugins

# sysconfig and init
%{__mkdir} -p %{buildroot}%{_sysconfdir}/rc.d/init.d
%{__mkdir} -p %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/rc.d/init.d/elasticsearch
%{__install} -m 755 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/elasticsearch

%{__mkdir} -p %{buildroot}%{_localstatedir}/run/elasticsearch
%{__mkdir} -p %{buildroot}%{_localstatedir}/lock/subsys/elasticsearch

# plugin-analysis-icu
%{__install} -D -m 755 plugins/analysis-icu/elasticsearch-analysis-icu-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/analysis-icu/elasticsearch-analysis-icu.jar
%{__install} -m 755 plugins/analysis-icu/lucene-icu-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/analysis-icu
%{__install} -m 755 plugins/analysis-icu/lucene-icu4j-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/analysis-icu

# plugin-cloud-aws
%{__install} -D -m 755 plugins/cloud-aws/elasticsearch-cloud-aws-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/cloud-aws/elasticsearch-cloud-aws.jar
%{__install} -m 755 plugins/cloud-aws/aws-java-sdk-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/cloud-aws
%{__install} -m 755 plugins/cloud-aws/commons-codec-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/cloud-aws
%{__install} -m 755 plugins/cloud-aws/commons-logging-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/cloud-aws

# plugin-hadoop
%{__install} -D -m 755 plugins/hadoop/elasticsearch-hadoop-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/hadoop/elasticsearch-hadoop.jar
%{__install} -m 755 plugins/hadoop/commons-logging-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/hadoop
%{__install} -m 755 plugins/hadoop/hadoop-core-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/hadoop

# plugin-lang-groovy
%{__install} -D -m 755 plugins/lang-groovy/elasticsearch-lang-groovy-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/lang-groovy/elasticsearch-lang-groovy.jar
%{__install} -m 755 plugins/lang-groovy/groovy-all-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/lang-groovy

# plugin-lang-javascript
%{__install} -D -m 755 plugins/lang-javascript/elasticsearch-lang-javascript-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/lang-javascript/elasticsearch-lang-javascript.jar
%{__install} -m 755 plugins/lang-javascript/rhino-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/lang-javascript

# plugin-lang-python
%{__install} -D -m 755 plugins/lang-python/elasticsearch-lang-python-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/lang-python/elasticsearch-lang-python.jar
%{__install} -m 755 plugins/lang-python/jython-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/lang-python

# plugin-mapper-attachments
%{__install} -D -m 755 plugins/mapper-attachments/elasticsearch-mapper-attachments-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/mapper-attachments/elasticsearch-mapper-attachments.jar
%{__install} -m 755 plugins/mapper-attachments/tika-app-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/mapper-attachments

# plugin-river-couchdb
%{__install} -D -m 755 plugins/river-couchdb/elasticsearch-river-couchdb-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/river-couchdb/elasticsearch-river-couchdb.jar

# plugin-river-rabbitmq
%{__install} -D -m 755 plugins/river-rabbitmq/elasticsearch-river-rabbitmq-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/river-rabbitmq/elasticsearch-river-rabbitmq.jar
%{__install} -m 755 plugins/river-rabbitmq/commons-io-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/river-rabbitmq
%{__install} -m 755 plugins/river-rabbitmq/amqp-client-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/river-rabbitmq

# plugin-river-twitter
%{__install} -D -m 755 plugins/river-twitter/elasticsearch-river-twitter-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/river-twitter/elasticsearch-river-twitter.jar
%{__install} -m 755 plugins/river-twitter/twitter4j-core-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/river-twitter

# plugin-river-wikipedia
%{__install} -D -m 755 plugins/river-wikipedia/elasticsearch-river-wikipedia-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/river-wikipedia/elasticsearch-river-wikipedia.jar

# plugin-transport-memcached
%{__install} -D -m 755 plugins/transport-memcached/elasticsearch-transport-memcached-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/transport-memcached/elasticsearch-transport-memcached.jar

# plugin-transport-thrift
%{__install} -D -m 755 plugins/transport-thrift/elasticsearch-transport-thrift-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/transport-thrift/elasticsearch-transport-thrift.jar
%{__install} -m 755 plugins/transport-thrift/es-libthrift-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/transport-thrift
%{__install} -m 755 plugins/transport-thrift/slf4j-api-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/transport-thrift
%{__install} -m 755 plugins/transport-thrift/slf4j-log4j12-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/transport-thrift

# plugin-transport-wares
%{__install} -D -m 755 plugins/transport-wares/elasticsearch-transport-wares-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/transport-wares/elasticsearch-transport-wares.jar

%pre
# create elasticsearch group
if ! getent group elasticsearch >/dev/null; then
        groupadd -r elasticsearch
fi

# create elasticsearch user
if ! getent passwd elasticsearch >/dev/null; then
        useradd -r -g elasticsearch -d %{_javadir}/%{name} \
            -s /sbin/nologin -c "You know, for search" elasticsearch
fi

%post
/sbin/chkconfig --add elasticsearch

%preun
if [ $1 -eq 0 ]; then
  /sbin/service elasticsearch stop >/dev/null 2>&1
  /sbin/chkconfig --del elasticsearch
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/rc.d/init.d/elasticsearch
%config(noreplace) %{_sysconfdir}/sysconfig/elasticsearch
%{_sysconfdir}/logrotate.d/elasticsearch
%dir %{_javadir}/elasticsearch
%{_javadir}/elasticsearch/bin/*
%{_javadir}/elasticsearch/lib/*
%dir %{_javadir}/elasticsearch/plugins
%config(noreplace) %{_sysconfdir}/elasticsearch
%doc LICENSE.txt  NOTICE.txt  README.textile
%defattr(-,elasticsearch,elasticsearch,-)
%dir %{_localstatedir}/lib/elasticsearch
%{_localstatedir}/run/elasticsearch
%dir %{_localstatedir}/log/elasticsearch

%files plugin-analysis-icu
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/analysis-icu
%{_javadir}/elasticsearch/plugins/analysis-icu/*

%files plugin-cloud-aws
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/cloud-aws
%{_javadir}/elasticsearch/plugins/cloud-aws/*

%files plugin-hadoop
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/hadoop
%{_javadir}/elasticsearch/plugins/hadoop/*

%files plugin-lang-groovy
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/lang-groovy
%{_javadir}/elasticsearch/plugins/lang-groovy/*

%files plugin-lang-javascript
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/lang-javascript
%{_javadir}/elasticsearch/plugins/lang-javascript/*

%files plugin-lang-python
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/lang-python
%{_javadir}/elasticsearch/plugins/lang-python/*

%files plugin-mapper-attachments
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/mapper-attachments
%{_javadir}/elasticsearch/plugins/mapper-attachments/*

%files plugin-river-couchdb
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/river-couchdb
%{_javadir}/elasticsearch/plugins/river-couchdb/*

%files plugin-river-rabbitmq
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/river-rabbitmq
%{_javadir}/elasticsearch/plugins/river-rabbitmq/*

%files plugin-river-twitter
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/river-twitter
%{_javadir}/elasticsearch/plugins/river-twitter/*

%files plugin-river-wikipedia
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/river-wikipedia
%{_javadir}/elasticsearch/plugins/river-wikipedia/*

%files plugin-transport-memcached
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/transport-memcached
%{_javadir}/elasticsearch/plugins/transport-memcached/*

%files plugin-transport-thrift
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/transport-thrift
%{_javadir}/elasticsearch/plugins/transport-thrift/*

%files plugin-transport-wares
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/transport-wares
%{_javadir}/elasticsearch/plugins/transport-wares/*


%changelog
* Sat Nov 26 2011 Tavis Aitken <tavisto@tavisto.net> - 0.18.4-1
- New upstream version

* Mon Oct 31 2011 Dan Carley <dan.carley@gmail.com> - 0.18.2-2
- Raise open files limit.

* Sat Oct 29 2011 Tavis Aitken <tavisto@tavisto.net> - 0.18.2-1
- New upstream version.

* Mon Jul 25 2011 Erick Tryzelaar erick.tryzelaar@gmail.com 0.17.1-1
- New Upstream version 

* Thu Jul 14 2011 Erick Tryzelaar erick.tryzelaar@gmail.com 0.16.4-1
- New Upstream version 
- Add analysis-icu, cloud-aws, hadoop, lang-groovy, lang-python,
  mapper-attachments, transport-memcached, transport-thrift, and
  transports-wares plugin subpackages

* Fri Jun 24 2011 Dan Everton dan.everton@wotifgroup.com 0.16.2-2
- Set plugins path so they are automatically detected by ES.

* Thu Jun 02 2011 Dan Everton dan.everton@wotifgroup.com 0.16.2-1
- New Upstream version 

* Wed May 11 2011 Tavis Aitken tavisto@tavisto.net 0.16.0-2
- Add lang-javascript plugin subpackage

* Thu Apr 28 2011 Tavis Aitken tavisto@tavisto.net 0.16.0-1
- New upstream version 

* Wed Apr 06 2011 Dan Carley <dan.carley@gmail.com> 0.15.2-2
- Moved data to /var/lib
- Allow customisation of paths.
- Allow customisation of memory and include settings.

* Mon Mar 07 2011 Tavis Aitken tavisto@tavisto.net 0.15.2-1
- New Upstream version 

* Mon Mar 07 2011 Tavis Aitken tavisto@tavisto.net 0.15.1-1
- New Upstream version 

* Mon Mar 01 2011 Tavis Aitken tavisto@tavisto.net 0.15.0-1
- New Upstream version 

* Mon Feb 28 2011 Tavis Aitken tavisto@tavisto.net 0.14.3-0
- New Upstream version 

* Sat Jan 29 2011 Tavis Aitken tavisto@tavisto.net 0.14.3-2
- Fixed the paths for the plugin sub-packages

* Sat Jan 29 2011 Tavis Aitken tavisto@tavisto.net 0.14.3-1
- Update to upstream version, complete with river plugin sub-packages

* Sat Jan 29 2011 Tavis Aitken tavisto@tavisto.net 0.14.2-3
- Fixed the user creation comment to not include a colon

* Fri Jan 21 2011  Tavis Aitken <tavisto@tavisto.net> - 0.14.2-2
- Fixed the logging.yml and logrotate.d configs

* Fri Jan 14 2011 Tavis Aitken <tavisto@tavisto.net> - 0.14.2-1
- New upstream version, and added specific arch suport for the sigar libraries.

* Tue Jan 4 2011 Tavis Aitken <tavisto@tavisto.net> - 0.14.1-1
- Initial package
