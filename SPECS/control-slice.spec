Summary: XenServer Control Slice
Name: control-slice
Version: 1.1.0
Release: 1%{dist}
License: GPL2
Group: Administration/System
Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/control-slice/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: libcgroup libcgroup-tools

%description
Control Path slice separating control path daemons to the separate cpu control group

%prep
%autosetup -p1
%build
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Reloads the daemons' configuration files
%post
systemctl daemon-reload >/dev/null 2>&1 || :

%files
%defattr(-,root,root)
%{_sysconfdir}/systemd/system/control.slice
%{_sysconfdir}/systemd/system/control-slice-rt.service
%{_sysconfdir}/systemd/system/*.service.d/slice.conf
%{_sysconfdir}/systemd/system/*.service.d/control-slice-rt-dep.conf
%{_sysconfdir}/xensource/bugtool/control-slice.xml
%{_sysconfdir}/xensource/bugtool/control-slice/stuff.xml
/opt/xensource/libexec/systemd_slice_pids

%changelog
* Fri Mar 02 2018 Edwin Török <edvin.torok@citrix.com> - v1.1.0-1
- Add sbd and xapi-clusterd to control-slice
- Add qemuback to service whitelist
- CP-24885: Add infrastructure to let services depend ability to set RT priority
- CP-24885: Enable sbd to assume RT priority

* Thu Jan 12 2017 Jonathan Davies <jonathan.davies@citrix.com> - 1.0.0-5
- CA-225067: No longer modify cgrules.conf
