Summary:	Media-Detect - media detecting scripts
Summary(de):	Media-Detect - Media erkennungs Scripts
Summary(pl):	Media-Detect - scrypty wykrywania mediów
Name:		Media-Detect
Version:	0.55
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.kde-apps.org/content/files/9820-%{name}-%{version}.tar.gz
# Source0-md5:	8e8a913e59e649528f71741246b2ca6d
Patch0:		%{name}_bash3.patch
URL:		http://www.kde-apps.org/content/show.php?content=9820
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Media-Detect is a script designed to make your multimedia shortcuts
more powerful and easier to configure. It is intended for use with
LinEAK, but can be called by any shortcuts or applications you like -
such as khotkeys - or executed from the command line.

%description -l de
Media-Detect ist ein Script dass entstanden ist um die configuration
und benutzung von Shortcuts maximal zu vereinfachen. Es wurde
geschrieben um es mit LinEAK zu kombinieren, aber jedes andere
Shortcut Programm - wie z.B. khotkeys - tut es auch, es kann auch von
der konsole gestartet werden.

%description -l pl
Media-Detect to skrypt powsta³y z my¶l± o maksymalnym uproszczeniu
konfiguracji oraz u¿yteczno¶ci skrótów klawiszowych. Z pocz±tku by³
my¶lany dla LinEAKa, ale równie dobrze mo¿na go uzywaæ np. z khotkeys
lub z konsoli.

%prep
%setup -q
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install media-detect $RPM_BUILD_ROOT%{_bindir}/
install media-menu $RPM_BUILD_ROOT%{_bindir}/
install configs/*.config $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog contact
%attr(755,root,root) %{_bindir}/media-detect
%attr(755,root,root) %{_bindir}/media-menu
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.config
