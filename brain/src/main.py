from recycling_system import RecyclingSystem

from envyaml import EnvYAML

if __name__ == '__main__':
    print(f"\Initializing system...\n")

    config = EnvYAML('config.yaml')
    recycling_system = RecyclingSystem(config)
    recycling_system.run()