%define	major 0
%define libname %mklibname %name %{major}
%define develname %mklibname %name -d

Summary:	msiLBC is low bitrate audio codec - plugin for mediastreamer
Name:		msilbc
Version:	2.0.3
Release:	%mkrel 1
License:	GPL2
Group:		System/Libraries
URL:		http://www.linphone.org
Source0:	http://download.savannah.gnu.org/releases/linphone/plugins/sources/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	autoconf2.5
BuildRequires:	automake
BuildRequires:	ortp-devel
BuildRequires:	linphone-devel 
BuildRequires:	libilbc-devel

%description
This package supplies the mediastreamer plugin for the iLBC audio
codec, which is necessary to use the codec with Linphone.
iLBC is low bitrate audio codec - plugin for mediastreamer.
Needed to build Google Talk libjingle voice call support with iLBC codec.


#--------------------------------------------------------------------
%package -n %{libname}
Summary:	Library files for msiLBC
Group:          System/Libraries

%description -n	%{libname}
This package supplies the mediastreamer plugin for the iLBC audio
codec, which is necessary to use the codec with Linphone.
iLBC is low bitrate audio codec - plugin for mediastreamer.
Needed to build Google Talk libjingle voice call support with iLBC codec.

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/mediastreamer/plugins/libmsilbc.so.%{major}*


#--------------------------------------------------------------------
%package -n %{develname}
Summary:	Development files for msiLBC library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package supplies the mediastreamer plugin for the iLBC audio
codec, which is necessary to use the codec with Linphone.
iLBC is low bitrate audio codec - plugin for mediastreamer.
Needed to build Google Talk libjingle voice call support with iLBC codec.

%files -n %{develname}
%defattr(-,root,root)
%doc README INSTALL AUTHORS COPYING NEWS
%{_libdir}/mediastreamer/plugins/libmsilbc.so
%{_libdir}/mediastreamer/plugins/libmsilbc.la


#--------------------------------------------------------------------
%prep
%setup -q

%build
export ILBC_CFLAGS='%{optflags}'
export ILBC_LIBS='%_libdir'
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


