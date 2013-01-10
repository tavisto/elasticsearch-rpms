%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-analysis-kuromoji
Version:        1.1.0
Release:        1%{?dist}
Summary:        ElasticSearch plugin for Lucene kuromoji analysis module

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-analysis-kuromoji

Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-analysis-kuromoji/elasticsearch-analysis-kuromoji-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19

%description
The Japanese (kuromoji) Analysis plugin integrates Lucene kuromoji
analysis module into elasticsearch.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/analysis-kuromoji

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/analysis-kuromoji/elasticsearch-analysis-kuromoji-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/analysis-kuromoji/elasticsearch-analysis-kuromoji.jar
%{__install} -m 755 plugins/analysis-kuromoji/lucene-kuromoji-*.jar -t %{buildroot}/%{base_install_dir}/plugins/analysis-kuromoji

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/analysis-kuromoji
%{base_install_dir}/plugins/analysis-kuromoji/*

%changelog
* Thu Jan 10 2013 Dan Everton dan.everton@wotifgroup.com 1.1.0-1
- Initial package

