#ifndef TRIANGLE_H
#define TRIANGLE_H

class Triangle : public Shape
{
	protected:
	double m_base;
	double m_height;
	
	public:
	double area() const;
	
};

#endif