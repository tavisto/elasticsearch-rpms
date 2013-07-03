%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-mapper-attachments
Version:        1.7.0
Release:        1%{?dist}
Summary:        ElasticSearch plugin to add attachment type

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-mapper-attachments

Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-mapper-attachments/elasticsearch-mapper-attachments-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.90

%description
The mapper attachments plugin adds the
attachment type to ElasticSearch using Tika.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/mapper-attachments

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/mapper-attachments/elasticsearch-mapper-attachments-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/mapper-attachments/elasticsearch-mapper-attachments.jar
%{__install} -D -m 755 plugins/mapper-attachments/*.jar -t %{buildroot}/%{base_install_dir}/plugins/mapper-attachments/

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/mapper-attachments
%{base_install_dir}/plugins/mapper-attachments/*

%changelog
* Wed Jul 03 2013 Nathan Milford <nathan@milford.io> 1.7.0-1
- New upstream version

* Tue Nov 27 2012 Tavis Aitken tavisto@tavisto.net 1.6.0-1
- New upstream version
- Fixed base_install_dir

* Wed Mar 21 2012 tavisto@tavisto.net 1.3.0-1
- New upstream version

* Tue Feb 22 2012 Sean Laurent 1.2.0-1
- Initial package

