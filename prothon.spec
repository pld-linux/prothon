
%define		pr_build	b711
%define		pr_libver	0.0

Summary:	Prototype-oriented scripting programming language
Summary(pl.UTF-8):	Zorientowany na prototypy skryptowy język programowania
Name:		prothon
Version:	0.1.2
Release:	2
License:	HCA
Group:		Development/Languages
Source0:	http://prothon.org/pub/prothon/%{name}-%{version}-%{pr_build}.tar.gz
# Source0-md5:	71bfef4e0269be720bc4236671bfdbfe
Source1:	http://prothon.org/pub/prothon/tutorial.zip
# Source1-md5:	d1b46ddf2b94c398f3a0e919bebd5bd1
URL:		http://prothon.org/
BuildRequires:	apr-util-devel
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	sqlite-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Prothon is a new object-centric language that gets rid of classes
altogether in the same way that Self does and regains the original
practical and fun sensibility of Python, an interpreted language with
object-oriented features that is practical, powerful, and fun to
program at the same time.

Python is the premiere interpreted language of choice, but over time
capabilities have been added to the core Python language, while
compatibility with earlier versions has been maintained, and Python
has became loaded with features, some quite complex. The metaclass is
an example of a recent feature addition. Even Python experts admit
that metaclasses are brain-achingly complex.

Prothon is also an industrial-strength alternative to Python and Self.
Prothon uses native threads and a 64-bit architecture to maximize
performance in applications such as multiple-cpu hosting. Prothon also
has a unique "blanket" security model and a transaction-based object
store built into the object structure.

For an in-depth look at Prototypes versus Classes, check
http://web.media.mit.edu/~lieber/Lieberary/OOP/Delegation/Delegation.html
link.

%description -l pl.UTF-8
Prothon jest nowym, zorientowanym obiektowo językiem programowania,
pozbawionym pojęcia klasy (w taki sam sposób, jak to robi Self z
językiem Java). Prothon zachowuje praktyczne i jednocześnie zabawne
właściwości Pythona, zauważalne w początkach jego powstawania - jest
interpretowanym, zorientowanym obiektowo językiem, umożliwiającym
programowanie w sposób praktyczny, skuteczny i jednocześnie wesoły.

Python jest świetnym językiem interpretowanym, lecz podczas jego
długiego rozwoju mnóstwo właściwości zostało dodanych do rdzenia
języka, przy jednoczesnym staraniu się o zachowanie kompatybilności z
wcześniejszymi wersjami, w wyniku czego Python stał się przeładowany
konstrukcjami, czasami bardzo złożonymi. Przykładem takiej konstrukcji
jest pojęcie metaklasy. Nawet eksperci Pythona uważają pojęcie to za
co najmniej ciężko zrozumiałe.

Prothon jest zatem mocną alternatywą dla Pythona i Selfa. Wykorzystuje
natywne implementacje wątków oraz 64-bitową architekturę w celu
zmaksymalizowania wydajności w aplikacjach takich jak wieloprocesorowy
hosting. Język posiada też unikalny model zapewniania bezpieczeństwa
oraz transakcyjny sposób przechowywania i modyfikacji właściwości
obiektów, wbudowany w strukturę obiektu.

W celu dokładnego porównania zorientowanego na prototypy i na klasy
programowania obiektowego warto zapoznać się z dokumentem dostępnym
pod linkiem
http://web.media.mit.edu/~lieber/Lieberary/OOP/Delegation/Delegation.html.

%package examples
Summary:	Example Prothon programs
Summary(pl.UTF-8):	Przykłady programy napisane w Prothonie
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Prothon programming
language. Theses programs were written as a simple tutorial, which
shows most common language features.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy napisane w języku Prothon.
Programy te napisane zostały w postaci prostego tutoriala
wprowadzającego programistę w kolejne możliwości tego języka
programowania.

%prep
%setup -q -n %{name}-%{version}-%{pr_build}
unzip -d . %{SOURCE1}

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/prothon-%{pr_libver},%{_examplesdir}/%{name}-%{version}}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/prothon-%{pr_libver}/*.{la,a}

cp -a tutorial/ $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.txt STATUS.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/prothon-%{pr_libver}
%attr(755,root,root) %{_libdir}/prothon-%{pr_libver}/*.so

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
