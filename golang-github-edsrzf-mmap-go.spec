# https://github.com/edsrzf/mmap-go
%global goipath github.com/edsrzf/mmap-go
%global commit  0bce6a6887123b67a60366d2c9fe2dfb74289d2e
%global date    20170318

%gometa

Name:           golang-github-edsrzf-mmap-go
Version:        0
Release:        0.6%{?dist}
Summary:        Portable mmap package for Go
License:        BSD

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.20170318git0bce6a6
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20170318.git0bce6a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170318.git0bce6a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170318.git0bce6a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170318.git0bce6a6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20170318.git0bce6a6
- First package for Fedora

