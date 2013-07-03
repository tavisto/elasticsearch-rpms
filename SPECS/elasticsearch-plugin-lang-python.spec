%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-lang-python
Version:        1.2.0
Release:        1%{?dist}
Summary:        ElasticSearch plugin to use Python for script execution

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-lang-python

Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-lang-python/elasticsearch-lang-python-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.90

%description
The Groovy language plugin allows to have Python
as the language of scripts to execute.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/lang-python

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/lang-python/elasticsearch-lang-python-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/lang-python/elasticsearch-lang-python.jar
%{__install} -D -m 755 plugins/lang-python/jython-standalone-*.jar -t %{buildroot}/%{base_install_dir}/plugins/lang-python/

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/lang-python
%{base_install_dir}/plugins/lang-python/*

%changelog
* Wed Jul 03 2013 Nathan Milford <nathan@milford.io> 1.2.0-1
- New upstream version

* Tue Nov 27 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-2
- Fixed base_install_dir

* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.1.0-0
- Initial package

