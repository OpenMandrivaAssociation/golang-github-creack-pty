# Run tests in check section.  Disable for bootstrapping
%bcond_without check

# This shuld be set before %%gometa
%global goipath		github.com/creack/pty
%global forgeurl	https://github.com/creack/pty
Version:			1.1.21

%gometa

Summary:		PTY interface for Go
Name:			golang-github-creack-pty
Release:		1
License:		MIT
Group:			Development/Other
URL:			%{gourl}
Source:			%{gosource}
BuildRequires:	compiler(golang)
Requires:		golang
BuildArch:		noarch

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
%forgeautosetup -q
%autopatch -p1

%build
export GO111MODULE=off
%gobuildroot
%gobuild -o _bin/go-pty

%install
export GO111MODULE=off
%goinstall

%check
%if %{with check}
%gochecks
%endif

