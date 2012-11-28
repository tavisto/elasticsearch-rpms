%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-hadoop
Version:        1.2.0
Release:        2%{?dist}
Summary:        ElasticSearch plugin to use Hadoop

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-hadoop

Source0:        https://github.com/downloads/elasticsearch/elasticsearch-hadoop/elasticsearch-hadoop-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19

%description
The Hadoop plugin allows to use Hadoop
as a shared gateway for ElasticSearch.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/hadoop

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/hadoop/elasticsearch-hadoop-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/hadoop/elasticsearch-hadoop.jar
%{__install} -D -m 755 plugins/hadoop/hadoop-core-0.20.204.0.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-cli-1.2.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/xmlenc-0.52.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-codec-1.4.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-math-2.1.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-configuration-1.6.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-collections-3.2.1.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-lang-2.4.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-digester-1.8.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-beanutils-1.7.0.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-beanutils-core-1.8.0.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-net-1.4.1.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop
%{__install} -D -m 755 plugins/hadoop/commons-el-1.0.jar -t %{buildroot}/%{base_install_dir}/plugins/hadoop

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/hadoop
%{base_install_dir}/plugins/hadoop/*

%changelog
* Tue Nov 27 2012 Tavis Aitken tavisto@tavisto.net 1.2.0-2
- Fixed base_install_dir

* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.2.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.3.0-0
- Initial package

