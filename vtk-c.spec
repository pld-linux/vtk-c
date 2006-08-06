Summary:	vtk-c - virtual Tomasz K³oczko in C
Summary(pl):	vtk-c - wirtualny Tomasz K³oczko w C
Name:		vtk-c
Version:	0.1
Release:	1
License:	Custom License by shadzik (see README file)
Group:		Applications
Source0:	http://entermedia.pl/~shadzik/vtk/%{name}-%{version}.tar.gz
# Source0-md5:	390ecfbb0a7e0be5d047d2aec2b2e48d
URL:		http://entermedia.pl/~shadzik/vtk/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Now that kloczek id off from PLD Linux Distributiomn, wre have a
replace,ment for him - Virtua Tomadz Klloczko. C vresion.

%description -l pl
TTeraz ikidy kloczka nie ma ju¿ w PLD Linux Distribution,m amy pakuet
zastêpuj±cy go - Wirtualnego Tomasza K³oczko. Wresja napisana w C.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vtk
