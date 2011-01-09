Name:           elasticsearch
Version:        0.14.1
Release:        1%{?dist}
Summary:        A distributed, highly available, RESTful search engine

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://www.elasticsearch.com
Source0:        https://github.com/downloads/%{name}/%{name}/%{name}-%{version}.tar.gz
Source1:        elasticsearch.init
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
%{__install} -p -m 744 bin/elasticsearch %{buildroot}%{_javadir}/%{name}/bin
%{__install} -p -m 744 bin/elasticsearch.in.sh %{buildroot}%{_javadir}/%{name}/bin
%{__install} -p -m 744 bin/plugin %{buildroot}%{_javadir}/%{name}/bin

#libs
%{__mkdir} -p %{buildroot}%{_javadir}/%{name}/lib/sigar
%{__install} -p -m 644 lib/*.jar %{buildroot}%{_javadir}/%{name}/lib
%{__install} -p -m 644 lib/sigar/* %{buildroot}%{_javadir}/%{name}/lib/sigar

# config
%{__mkdir} -p %{buildroot}%{_sysconfdir}/elasticsearch 
%{__install} -m 644 config/* %{buildroot}%{_sysconfdir}/%{name}

# data
%{__mkdir} -p %{buildroot}%{_javadir}/%{name}/data

# logs
%{__mkdir} -p %{buildroot}%{_localstatedir}/log/%{name}

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
            -s /sbin/nologin -c "Elasticsearch, you know for search." elasticsearch 
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
%defattr(-,elasticsearch,elasticsearch,-)
%{_sysconfdir}/init.d/elasticsearch
%{_sysconfdir}/elasticsearch
%{_localstatedir}/run/elasticsearch
%dir %{_javadir}/elasticsearch
%dir %{_localstatedir}/log/elasticsearch
%{_javadir}/elasticsearch/*
%doc LICENSE.txt  NOTICE.txt  README.textile

%changelog
* Tue Jan 4 2011 Tavis Aitken <tavisto@tavisto.net> - 0.14.1-1
- Initial package
