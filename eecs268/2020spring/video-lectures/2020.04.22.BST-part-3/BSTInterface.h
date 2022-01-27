
//ItemType: What is being stored in the tree?
//KeyType: What type is used to search for an Item?
tempate <typename ItemType, typename KeyType>
class BinarySearchTreeInterface
{
    public:
    virtual ~BinarySearchTreeInterface(){}
    virtual void add(ItemType entry) = 0;
    virtual ItemType search(KeyType key) const = 0;
    virtual void clear() = 0;
    //More methods to come in next lab
};