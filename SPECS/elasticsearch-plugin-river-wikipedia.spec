%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-river-wikipedia
Version:        1.1.0
Release:        2%{?dist}
Summary:        ElasticSearch plugin to index Wikipedia

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-river-wikipedia

Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-river-wikipedia/elasticsearch-river-wikipedia-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19

%description
The Wikipedia River plugin allows indexng of Wikipedia

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/river-wikipedia

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/river-wikipedia/elasticsearch-river-wikipedia-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/river-wikipedia/elasticsearch-river-wikipedia.jar

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/river-wikipedia
%{base_install_dir}/plugins/river-wikipedia/*

%changelog
* Tue Nov 27 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-2
- Fixed base_install_dir

* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.1.0-0
- Initial package

