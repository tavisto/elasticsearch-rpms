%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-jetty
Version:        0.19.8
Release:        1%{?dist}
Summary:        ElasticSearch plugin to add attachment type

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/sonian/elasticsearch-jetty

Source0:        https://github.com/downloads/sonian/elasticsearch-jetty/elasticsearch-jetty-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19

%description
The elasticsearch-jetty plugin brings full power of Jetty and adds several new features to elasticsearch. With this plugin elasticsearch can now handle SSL connections, support basic authentication, and log all or some incoming requests in plain text or json formats.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/plugin-jetty

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}

# libs
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__cp} -r plugins/plugin-jetty %{buildroot}/%{base_install_dir}/plugins/jetty

# config
%{__mkdir} -p %{buildroot}%{_sysconfdir}/elasticsearch/plugins/jetty
%{__install} -m 644 plugins/plugin-jetty/config/jetty.xml %{buildroot}%{_sysconfdir}/elasticsearch/plugins/jetty

%files
%defattr(-,root,root,-)
%{base_install_dir}/plugins/jetty
%dir %{_sysconfdir}/elasticsearch/plugins/jetty
%config(noreplace) %{_sysconfdir}/elasticsearch/plugins/jetty/jetty.xml

%changelog
* Tue Aug 21 2012 manuel.vacelet@enalean.com 0.19.8-1
- Initial package

