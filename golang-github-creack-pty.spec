%global debug_package %{nil}

# Run tests in check section
%bcond_without check

# https://github.com/creack/pty
%global goipath		github.com/creack/pty
%global forgeurl	https://github.com/creack/pty
Version:		1.1.21

%gometa

Summary:	PTY interface for Go
Name:		golang-github-creack-pty

Release:	1
Source0:	https://github.com/creack/pty/archive/v%{version}/pty-%{version}.tar.gz
URL:		https://github.com/creack/pty
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)

%description
Pty is a Go package for using unix pseudo-terminals.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n pty-%{version}

%build
%gobuildroot
for cmd in $(ls -1 _bin) ; do
	install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done
#gobuild -o _bin/go-pty

%install
%goinstall
for cmd in $(ls -1 _bin) ; do
	install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done

%check
%if %{with check}
%gochecks
%endif

