%define abiquo_basedir /opt/abiquo

Name:     abiquo-client-community
Version:  1.7
Release:  4%{?dist}%{?buildstamp}
Summary:  Abiquo Flex Client
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  client.war
Source1:  index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core
BuildRequires: /usr/bin/unzip
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package contains the community client component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/client/ %{SOURCE0}
cp %{SOURCE1} $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/ROOT/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tomcat/webapps/client
%{abiquo_basedir}/tomcat/webapps/ROOT

%changelog
* Mon Feb 14 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- updated release string

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- updated client index.html

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- set buildarch to noarch

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-1
- Initial Release
