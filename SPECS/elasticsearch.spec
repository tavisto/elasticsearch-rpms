%define debug_package %{nil}

Name:           elasticsearch
Version:        0.14.2
Release:        3%{?dist}
Summary:        A distributed, highly available, RESTful search engine

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            http://www.elasticsearch.com
Source0:        https://github.com/downloads/%{name}/%{name}/%{name}-%{version}.tar.gz
Source1:        init.d-elasticsearch
Source2:        logrotate.d-elasticsearch
Source3:        config-logging.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       jpackage-utils
Requires:       java

Requires(post): chkconfig initscripts
Requires(pre):  chkconfig initscripts
Requires(pre):  shadow-utils

%description
A distributed, highly available, RESTful search engine

%prep
%setup -q -n %{name}-%{version}

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
%{__mkdir} -p %{buildroot}%{_javadir}/%{name}/data

# logs
%{__mkdir} -p %{buildroot}%{_localstatedir}/log/%{name}
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/elasticsearch

# plugins 
%{__mkdir} -p %{buildroot}%{_javadir}/%{name}/plugins

# sysconfig and init
%{__mkdir} -p %{buildroot}%{_sysconfdir}/{init.d,sysconfig}
%{__install} -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/elasticsearch

%{__mkdir} -p %{buildroot}%{_localstatedir}/run/elasticsearch
%{__mkdir} -p %{buildroot}%{_localstatedir}/lock/subsys/elasticsearch

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
%{_sysconfdir}/init.d/elasticsearch
%{_sysconfdir}/logrotate.d/elasticsearch
%dir %{_javadir}/elasticsearch
%{_javadir}/elasticsearch/*
%config(noreplace) %{_sysconfdir}/elasticsearch
%doc LICENSE.txt  NOTICE.txt  README.textile
%defattr(-,elasticsearch,elasticsearch,-)
%{_javadir}/elasticsearch/data
%{_localstatedir}/run/elasticsearch
%dir %{_localstatedir}/log/elasticsearch

%changelog
* Sat Jan 29 2011 Tavis Aitken tavisto@tavisto.net 0.14.2-3
- Fixed the user creation comment to not include a colon
    
* Fri Jan 21 2011  Tavis Aitken <tavisto@tavisto.net> - 0.14.2-2
- Fixed the logging.yml and logrotate.d configs

* Fri Jan 14 2011 Tavis Aitken <tavisto@tavisto.net> - 0.14.2-1
- New upstream version, and added specific arch suport for the sigar libraries.

* Tue Jan 4 2011 Tavis Aitken <tavisto@tavisto.net> - 0.14.1-1
- Initial package
