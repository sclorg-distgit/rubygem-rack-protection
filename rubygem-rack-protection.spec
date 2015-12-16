%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name rack-protection

%global bootstrap 1

Summary:        Ruby gem that protects against typical web attacks
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.5.0
Release:        1%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://github.com/rkh/rack-protection
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires:       %{?scl_prefix_ruby}ruby(release)
Requires:       %{?scl_prefix_ruby}ruby(rubygems)
Requires:       %{?scl_prefix}rubygem(rack)
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
%if 0%{bootstrap} < 1
BuildRequires:  %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires:  %{?scl_prefix}rubygem(rack)
BuildRequires:  %{?scl_prefix}rubygem(rspec-core)
BuildRequires:  %{?scl_prefix}rubygem(rack-test)
%endif
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem protects against typical web attacks.
Should work for all Rack apps, including Rails.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description	doc
This package contains documentation for %{pkg_name}.

%prep
%setup -q -c -T
%{?scl:scl enable %scl - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}
rm .%{gem_instdir}/%{gem_name}.gemspec
rm .%{gem_cache}

# Fix permissions
# https://github.com/rkh/rack-protection/pull/93
find .%{gem_instdir}/{lib,spec} -type f | xargs chmod 0644

%build

%check
%if 0%{bootstrap} < 1
pushd .%{gem_instdir}
%{?scl:scl enable %scl - << \EOF}
rspec spec
%{?scl:EOF}
popd
%endif

%install
%{__mkdir_p} %{buildroot}%{gem_dir}
cp -rv .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/License

%files doc
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%doc %{gem_docdir}

%changelog
* Fri Jan 16 2015 Josef Stribny <jstribny@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Thu Nov 21 2013 Josef Stribny <jstribny@redhat.com> - 1.2.0-9
- Run test suite

* Thu Jun 13 2013 Josef Stribny <jstribny@redhat.com> - 1.2.0-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-7
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-6
- Allowed tests running.

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-5
- Rebuilt for scl.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-4
- Set %%bootstrap to 0 to allow tests.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-3
- Rebuilt for Ruby 1.9.3.
- Introduced bootstrap to deal with dependency loop.

* Mon Jan 03 2012 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-2
- Fixed BR
- Marked documentation file with doc tag
- Changed the way how to run rspec tests

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-1
- Initial import
