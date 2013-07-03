%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-river-twitter
Version:        1.4.0
Release:        1%{?dist}
Summary:        ElasticSearch plugin to hook into Twitter

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-river-twitter

Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-river-twitter/elasticsearch-river-twitter-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.90

%description
The Twitter River plugin allows index twitter stream.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/river-twitter

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/river-twitter/elasticsearch-river-twitter-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/river-twitter/elasticsearch-river-twitter.jar
%{__install} -D -m 755 plugins/river-twitter/twitter4j-stream-*.jar -t %{buildroot}/%{base_install_dir}/plugins/river-twitter/
%{__install} -D -m 755 plugins/river-twitter/twitter4j-core-*.jar -t %{buildroot}/%{base_install_dir}/plugins/river-twitter/

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/river-twitter
%{base_install_dir}/plugins/river-twitter/*

%changelog
* Wed Jul 03 2013 Nathan Milford <nathan@milford.io> 1.4.0-1
- New upstream version

* Tue Nov 27 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-2
- Fixed base_install_dir

* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.1.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.1.0-0
- Initial package

