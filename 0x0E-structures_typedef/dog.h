int _putchrar(char c);
/**
 * struct dog - best freiend
 * @name: doggo's name
 * äge: doggo's age
 * @owner: owner's name
 */
typedef struct dog
{
	char *name;
	float age;
	char *owner;
}dog_t;
void init_dog(struct dog *d, char *name, float age, char *owner);
