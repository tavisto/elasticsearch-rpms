%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-river-rabbitmq
Version:        1.6.0
Release:        1%{?dist}
Summary:        ElasticSearch plugin to hook into RabbitMQ

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-river-rabbitmq

Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-river-rabbitmq/elasticsearch-river-rabbitmq-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.90

%description
The RabbitMQ River plugin allows index
bulk format messages into elasticsearch.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/river-rabbitmq

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/river-rabbitmq/elasticsearch-river-rabbitmq-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/river-rabbitmq/elasticsearch-river-rabbitmq.jar
%{__install} -D -m 755 plugins/river-rabbitmq/amqp-client-*.jar -t %{buildroot}/%{base_install_dir}/plugins/river-rabbitmq/

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/river-rabbitmq
%{base_install_dir}/plugins/river-rabbitmq/*

%changelog
* Wed Jul 03 2013 Nathan Milford <nathan@milford.io> 1.6.0-1
- New upstream version

* Tue Nov 27 2012 Tavis Aitken tavisto@tavisto.net 1.4.0-1
- New upstream version

* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.1.0-0
- Initial package
