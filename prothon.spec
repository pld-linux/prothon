
%define		pr_build	b711
%define		pr_libver	0.0

Summary:	Prototype-oriented scripting programming language
Summary(pl):	Zorientowany na prototypy skryptowy j�zyk programowania
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
BuildRequires:	boost-regex-devel
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

%description -l pl
Prothon jest nowym, zorientowanym obiektowo j�zykiem programowania,
pozbawionym poj�cia klasy (w taki sam spos�b, jak to robi Self z
j�zykiem Java). Prothon zachowuje praktyczne i jednocze�nie zabawne
w�a�ciwo�ci Pythona, zauwa�alne w pocz�tkach jego powstawania - jest
interpretowanym, zorientowanym obiektowo j�zykiem, umo�liwiaj�cym
programowanie w spos�b praktyczny, skuteczny i jednocze�nie weso�y.

Python jest �wietnym j�zykiem interpretowanym, lecz podczas jego
d�ugiego rozwoju mn�stwo w�a�ciwo�ci zosta�o dodanych do rdzenia
j�zyka, przy jednoczesnym staraniu si� o zachowanie kompatybilno�ci z
wcze�niejszymi wersjami, w wyniku czego Python sta� si� prze�adowany
konstrukcjami, czasami bardzo z�o�onymi. Przyk�adem takiej konstrukcji
jest poj�cie metaklasy. Nawet eksperci Pythona uwa�aj� poj�cie to za
co najmniej ci�ko zrozumia�e.

Prothon jest zatem mocn� alternatyw� dla Pythona i Selfa. Wykorzystuje
natywne implementacje w�tk�w oraz 64-bitow� architektur� w celu
zmaksymalizowania wydajno�ci w aplikacjach takich jak wieloprocesorowy
hosting. J�zyk posiada te� unikalny model zapewniania bezpiecze�stwa
oraz transakcyjny spos�b przechowywania i modyfikacji w�a�ciwo�ci
obiekt�w, wbudowany w struktur� obiektu.

W celu dok�adnego por�wnania zorientowanego na prototypy i na klasy
programowania obiektowego warto zapozna� si� z dokumentem dost�pnym
pod linkiem
http://web.media.mit.edu/~lieber/Lieberary/OOP/Delegation/Delegation.html.

%package examples
Summary:	Example Prothon programs
Summary(pl):	Przyk�ady programy napisane w Prothonie
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Prothon programming
language. Theses programs were written as a simple tutorial, which
shows most common language features.

%description examples -l pl
Ten pakiet zawiera przyk�adowe programy napisane w j�zyku Prothon.
Programy te napisane zosta�y w postaci prostego tutoriala
wprowadzaj�cego programist� w kolejne mo�liwo�ci tego j�zyka
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

cp -ar tutorial/ $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
