import click
import yaml
import os


@click.command()
@click.option('--domain', prompt='Domain')
@click.option('--type', 'site_type', prompt='Site type (shop/blog)')
@click.option('--email', prompt='Admin email')
@click.option('--admin-user', default='admin', show_default=True)
@click.option('--admin-password', prompt='Admin password', hide_input=True, confirmation_prompt=True)
def create(domain, site_type, email, admin_user, admin_password):

    profile_path = f"profile/{site_type}/profile.yaml"

    if not os.path.exists(profile_path):
        print("❌ profile not found")
        return

    with open(profile_path) as f:
        profile = yaml.safe_load(f)

    config = {
        "site": {
            "domain": domain,
            "type": site_type
        },
        "wordpress": {
            "admin": {
                "username": admin_user,
                "password": admin_password,
                "email": email
            },
            "theme": profile["wordpress"]["theme"],
            "plugins": profile["wordpress"]["plugins"]
        }
    }

    site_name = domain.replace(".", "-")

    os.makedirs(f"sites/{site_name}", exist_ok=True)

    with open(f"sites/{site_name}/values.yaml", "w") as f:
        yaml.safe_dump(config, f, sort_keys=False)

    print(f"Site config created: sites/{site_name}/values.yaml")


if __name__ == "__main__":
    create()