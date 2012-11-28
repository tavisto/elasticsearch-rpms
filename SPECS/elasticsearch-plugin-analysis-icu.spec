%define debug_package %{nil}
%define base_install_dir %{_javadir}/{%name}

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-analysis-icu
Version:        1.4.0
Release:        1%{?dist}
Summary:        ElasticSearch plugin for Lucene ICU

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-analysis-icu

Source0:        https://github.com/downloads/elasticsearch/elasticsearch-analysis-icu/elasticsearch-analysis-icu-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19

%description
The ICU Analysis plugin for ElasticSearch integrates Lucene ICU module
into elasticsearch, adding ICU relates analysis components.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/analysis-icu

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/analysis-icu/elasticsearch-analysis-icu-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/analysis-icu/elasticsearch-analysis-icu.jar
%{__install} -m 755 plugins/analysis-icu/lucene-icu-*.jar -t %{buildroot}/%{base_install_dir}/plugins/analysis-icu
%{__install} -m 755 plugins/analysis-icu/icu4j-*.jar -t %{buildroot}/%{base_install_dir}/plugins/analysis-icu

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/analysis-icu
%{base_install_dir}/plugins/analysis-icu/*

%changelog
* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.2.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.2.0-0
- Initial package
