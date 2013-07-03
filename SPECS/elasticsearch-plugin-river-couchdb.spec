%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-river-couchdb
Version:        1.2.0
Release:        1%{?dist}
Summary:        ElasticSearch plugin to hook into CouchDB

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-river-couchdb

Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-river-couchdb/elasticsearch-river-couchdb-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.90

%description
The CouchDB River plugin allows to hook into
couchdb _changes feed and automatically index it into elasticsearch.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/river-couchdb

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/river-couchdb/elasticsearch-river-couchdb-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/river-couchdb/elasticsearch-river-couchdb.jar

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/river-couchdb
%{base_install_dir}/plugins/river-couchdb/*

%changelog
* Wed Jul 03 2013 Nathan Milford <nathan@milford.io> 1.2.0-1
- New upstream version

* Tue Nov 27 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-2
- Fixed the base_install_dir to properly place the plugin

* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.1.0-0
- Initial package

