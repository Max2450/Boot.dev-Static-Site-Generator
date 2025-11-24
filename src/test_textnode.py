import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(repr(node), "TextNode(This is a text node, italic, None)")

    def test_link_node(self):
        node = TextNode("Click here", TextType.LINK, url="http://example.com")
        self.assertEqual(node.url, "http://example.com")
        self.assertEqual(repr(node), "TextNode(Click here, link, http://example.com)")

    def test_image_node(self):
        node = TextNode("Image description", TextType.IMAGE, url="http://example.com/image.png")
        self.assertEqual(node.url, "http://example.com/image.png")
        self.assertEqual(repr(node), "TextNode(Image description, image, http://example.com/image.png)")


if __name__ == "__main__":
    unittest.main()