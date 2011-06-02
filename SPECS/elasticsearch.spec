%define debug_package %{nil}

Name:           elasticsearch
Version:        0.16.2
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
Source5:        http://elasticsearch.googlecode.com/svn/plugins/river-couchdb/elasticsearch-river-couchdb-%{version}.zip
Source6:        http://elasticsearch.googlecode.com/svn/plugins/river-rabbitmq/elasticsearch-river-rabbitmq-%{version}.zip
Source7:        http://elasticsearch.googlecode.com/svn/plugins/river-twitter/elasticsearch-river-twitter-%{version}.zip
Source8:        http://elasticsearch.googlecode.com/svn/plugins/river-wikipedia/elasticsearch-river-wikipedia-%{version}.zip
Source9:        http://elasticsearch.googlecode.com/svn/plugins/lang-javascript/elasticsearch-lang-javascript-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       jpackage-utils
Requires:       java

Requires(post): chkconfig initscripts
Requires(pre):  chkconfig initscripts
Requires(pre):  shadow-utils

%description
A distributed, highly available, RESTful search engine

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

%package plugin-lang-javascript
BuildArch:      noarch
Summary:        A lang plugin to add support for JavaScript
Group:          System Environment/Daemons
Requires: elasticsearch = %{version}

%description plugin-lang-javascript
A lang plugin to add support for JavaScript

%prep
%setup -q -n %{name}-%{version}
unzip %{SOURCE5}
unzip %{SOURCE6}
unzip %{SOURCE7}
unzip %{SOURCE8}
unzip %{SOURCE9}

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

# plugin-river-couchdb
%{__install} -D -m 755 elasticsearch-river-couchdb-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/river-couchdb/elasticsearch-river-couchdb.jar

# plugin-river-rabbitmq
%{__install} -D -m 755 elasticsearch-river-rabbitmq-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/river-rabbitmq/elasticsearch-river-rabbitmq.jar
%{__install} -m 755 commons-io-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/river-rabbitmq
%{__install} -m 755 amqp-client-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/river-rabbitmq

# plugin-river-twitter
%{__install} -D -m 755 elasticsearch-river-twitter-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/river-twitter/elasticsearch-river-twitter.jar
%{__install} -m 755 twitter4j-core-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/river-twitter

# plugin-river-wikipedia
%{__install} -D -m 755 elasticsearch-river-wikipedia-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/river-wikipedia/elasticsearch-river-wikipedia.jar

# plugin-lang-javascript-
%{__install} -D -m 755 elasticsearch-lang-javascript-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/lang-javascript/elasticsearch-lang-javascript.jar
%{__install} -m 755 js-*.jar -t %{buildroot}%{_javadir}/%{name}/plugins/lang-javascript

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

%files plugin-lang-javascript
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/lang-javascript
%{_javadir}/elasticsearch/plugins/lang-javascript/*


%changelog
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
