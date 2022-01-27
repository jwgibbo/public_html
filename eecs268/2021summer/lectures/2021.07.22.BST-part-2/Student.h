

class Student
{
	private:
	std::string m_name;
	int m_id;
	double m_gpa;
	
	
	public:
	Student();
	//other student methods
	
	bool operator<(const Student& rhs) const;
	bool operator==(const Student& rhs) const;
	bool operator>(const Student& rhs) const;
	
	bool operator<(int id) const;
	bool operator==(int id) const;
};
