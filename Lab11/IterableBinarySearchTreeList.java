import java.util.Iterator;

public class IterableBinarySearchTreeList<T> {
	
	protected int count;
	protected BinaryTreeNode<T> root;
	
	public IterableBinarySearchTreeList() {
		count = 0;
		root = null;
	}
	
	public Iterator<T> iteratorInOrderDescending() {
		ArrayUnorderedList<T> placeHolder = new ArrayUnorderedList<T>();
		descendingInOrder (root, placeHolder);

		return placeHolder.iterator();
	}
	
	private void descendingInOrder(BinaryTreeNode<T> node, ArrayUnorderedList<T> tempList) {
		if (node != null)
		{
			descendingInOrder (node.getRight(), tempList);
			tempList.addToRear(node.getElement());
			descendingInOrder (node.getLeft(), tempList);
		}
	}
}
