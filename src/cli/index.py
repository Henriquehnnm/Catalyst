import fire


class Catalyst:
    def test(self, name="World"):
        return f"Hello {name}!"


if __name__ == "__main__":
    fire.Fire(Catalyst)
