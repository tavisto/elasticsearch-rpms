%define debug_package %{nil}
%define base_install_dir %{_javadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-cloud-aws
Version:        1.10.0
Release:        1%{?dist}
Summary:        ElasticSearch plugin to use EC2 and S3

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-cloud-aws

Source0:        https://github.com/downloads/elasticsearch/elasticsearch-cloud-aws/elasticsearch-cloud-aws-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19

%description
The AWS Cloud plugin allows to use AWS EC2 API for the
unicast discovery mechanism as well as using S3 as a shared gateway.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/cloud-aws

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/cloud-aws/elasticsearch-cloud-aws-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/cloud-aws/elasticsearch-cloud-aws.jar
%{__install} -D -m 755 plugins/cloud-aws/aws-java-sdk-1.3.18.jar -t %{buildroot}/%{base_install_dir}/plugins/cloud-aws
%{__install} -D -m 755 plugins/cloud-aws/commons-logging-1.1.1.jar -t %{buildroot}/%{base_install_dir}/plugins/cloud-aws
%{__install} -D -m 755 plugins/cloud-aws/commons-codec-1.3.jar -t %{buildroot}/%{base_install_dir}/plugins/cloud-aws
%{__install} -D -m 755 plugins/cloud-aws/httpclient-4.1.1.jar -t %{buildroot}/%{base_install_dir}/plugins/cloud-aws
%{__install} -D -m 755 plugins/cloud-aws/httpcore-4.1.jar -t %{buildroot}/%{base_install_dir}/plugins/cloud-aws

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/cloud-aws
%{base_install_dir}/plugins/cloud-aws/*

%changelog
* Fri Dec 28 2012 Chris Schuld chris@chrisschuld.com 1.10.0
- New upstream version

* Tue Nov 27 2012 Tavis Aitken tavisto@tavisto.net 1.9.0-1
- New upstream version
- Fixed base_install_dir

* Wed Mar 21 2012 Tavis Aitken tavisto@tavisto.net 1.3.0-1
- Tweaked to make the package conform to fedora build specs

* Tue Feb 22 2012 Sean Laurent 1.3.0-0
- Initial package

