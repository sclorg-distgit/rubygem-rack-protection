%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name rack-protection

%global bootstrap 0

Summary:        Ruby gem that protects against typical web attacks
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        1.5.3
Release:        4%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://github.com/rkh/rack-protection
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires:       %{?scl_prefix_ruby}ruby(release)
Requires:       %{?scl_prefix_ruby}ruby(rubygems)
Requires:       %{?scl_prefix}rubygem(rack)
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
%if 0%{bootstrap} < 1
BuildRequires:  %{?scl_prefix_ruby}rubygem(test-unit)
BuildRequires:  %{?scl_prefix}rubygem(rack)
BuildRequires:  %{?scl_prefix}rubygem(rspec) < 3
BuildRequires:  %{?scl_prefix}rubygem(rack-test)
%endif
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem protects against typical web attacks.
Should work for all Rack apps, including Rails.

%package        doc
Summary:        Documentation for %{pkg_name}
Group:          Documentation

Requires:       %{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description    doc
This package contains documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}
rm .%{gem_instdir}/%{gem_name}.gemspec
rm .%{gem_cache}

%build

%check
%if 0%{bootstrap} < 1
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
rspec spec
%{?scl:EOF}
popd
%endif

%install
%{__mkdir_p} %{buildroot}%{gem_dir}
cp -rv .%{gem_dir}/* %{buildroot}%{gem_dir}

# Fix presmissions.
# https://github.com/rkh/rack-protection/pull/93
chmod a-x %{buildroot}%{gem_instdir}/lib/rack/protection/base.rb
chmod a-x %{buildroot}%{gem_instdir}/spec/protection_spec.rb

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
* Wed Feb 10 2016 Dominic Cleal <dcleal@redhat.com> 1.5.3-4
- Enable package check

* Fri Jan 22 2016 Dominic Cleal <dcleal@redhat.com> 1.5.3-3
- Rebuild for sclo-ror42 SCL

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Vít Ondruch <vondruch@redhat.com> - 1.5.3-1
- Update to rack-protection 1.5.3.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Michal Fojtik <mfojtik@redhat.com> - 1.5.0-1
- Release 1.5.0

* Tue Mar 05 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Feb 22 2013 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-2
- Fixed rspec dependency

* Thu Feb 21 2013 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-1
- Release 1.3.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-4
- Set %%bootstrap to 0 to allow tests.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.0-3
- Rebuilt for Ruby 1.9.3.
- Introduced bootstrap to deal with dependency loop.

* Tue Jan 03 2012 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-2
- Fixed BR
- Marked documentation file with doc tag
- Changed the way how to run rspec tests

* Mon Jan 02 2012 Michal Fojtik <mfojtik@redhat.com> - 1.2.0-1
- Initial import
