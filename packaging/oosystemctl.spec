Name:           oosystemctl
Version:        0.1.0
Release:        1%{?dist}
Summary:        Capability-bounded service, socket, and timer manager for systemd userland.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosystemctl
Source0:        oosystemctl-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosystemctl is a sovereign, capability-bounded SYSTEMD CONTROL written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosystemctl
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosystemctl-uninstall

%files
/usr/bin/oosystemctl
/usr/bin/oosystemctl-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
