%define debug_package %{nil}
%define project elasticsearch

Name:           elasticsearch-plugin-river-couchdb
Version:        1.0.0
Release:        1%{?dist}
Summary:        An Elasticsearch river plugin to index from a couchdb database

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            http://www.elasticsearch.com
Source0:        https://github.com/downloads/%{project}/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       jpackage-utils
Requires:       java
Requires:       elasticsearch

%description
The CouchDB River allows to automatically index couchdb and make it searchable using the excellent _changes stream couchdb provides

%prep
%setup -q -n %{name}-%{version}
%{__mkdir} -p plugins

%build
true

%install
rm -rf $RPM_BUILD_ROOT
# plugin-river-couchdb
%{__install} -D -m 755 plugins/river-couchdb/elasticsearch-river-couchdb-%{version}.jar %{buildroot}%{_javadir}/%{name}/plugins/river-couchdb/elasticsearch-river-couchdb.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_javadir}/elasticsearch/plugins/river-couchdb
%{_javadir}/elasticsearch/plugins/river-couchdb/*

%changelog
* Sun Mar 11 2012 tavisto@tavisto.net 1.0.0-1
- Initial package
