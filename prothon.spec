
%define		pr_build	b585
%define		pr_libver	0.0

Summary:	Prototype-oriented scripting programming language
Summary(pl):	Zorientowany na prototypy skryptowy jêzyk programowania
Name:		prothon
Version:	0.1.1
Release:	1
License:	HCA
Group:		Development/Languages
Source0:	http://prothon.org/pub/prothon/%{name}-%{version}-%{pr_build}.tar.gz
# Source0-md5:	5b47e41707d7a08310c3504339e59394
URL:		http://prothon.org/
BuildRequires:	apr-util-devel
BuildRequires:	bison
BuildRequires:	boost-regex-devel
BuildRequires:	sqlite-devel
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
Prothon jest nowym, zorientowanym obiektowo jêzykiem programowania,
pozbawionym pojêcia klasy (w taki sam sposób, jak to robi Self z
jêzykiem Java). Prothon zachowuje praktyczne i jednocze¶nie zabawne
w³a¶ciwo¶ci Pythona, zauwa¿alne w pocz±tkach jego powstawania - jest
interpretowanym, zorientowanym obiektowo jêzykiem, umo¿liwiaj±cym
programowanie w sposób praktyczny, skuteczny i jednocze¶nie weso³y.

Python jest ¶wietnym jêzykiem interpretowanym, lecz podczas jego
d³ugiego rozwoju mnóstwo w³a¶ciwo¶ci zosta³o dodanych do rdzenia
jêzyka, przy jednoczesnym staraniu siê o zachowanie kompatybilno¶ci z
wcze¶niejszymi wersjami, w wyniku czego Python sta³ siê prze³adowany
konstrukcjami, czasami bardzo z³o¿onymi. Przyk³adem takiej konstrukcji
jest pojêcie metaklasy. Nawet eksperci Pythona uwa¿aj± pojêcie to za
co najmniej ciê¿ko zrozumia³e.

Prothon jest zatem mocn± alternatyw± dla Pythona i Selfa. Wykorzystuje
natywne implementacje w±tków oraz 64-bitow± architekturê w celu
zmaksymalizowania wydajno¶ci w aplikacjach takich jak wieloprocesorowy
hosting. Jêzyk posiada te¿ unikalny model zapewniania bezpieczeñstwa
oraz transakcyjny sposób przechowywania i modyfikacji w³a¶ciwo¶ci
obiektów, wbudowany w strukturê obiektu.

W celu dok³adnego porównania zorientowanego na prototypy i na klasy
programowania obiektowego warto zapoznaæ siê z dokumentem dostêpnym
pod linkiem
http://web.media.mit.edu/~lieber/Lieberary/OOP/Delegation/Delegation.html.

%prep
%setup -q -n %{name}-%{version}-%{pr_build}

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/prothon-%{pr_libver}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt LICENSE STATUS.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/prothon-%{pr_libver}
%attr(755,root,root) %{_libdir}/prothon-%{pr_libver}/*.so
