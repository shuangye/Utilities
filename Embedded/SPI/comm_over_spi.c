typedef unsigned char byte_t;
typedef unsigned char uint8_t;
typedef unsigned int  uint32_t;
typedef int           int32_t;

/* 
  application layer
  semantics: TX, RX, split into frames
 */

typedef enum
{
	SPI_TRANS_TYPE_NONE = 0,
	SPI_TRANS_TYPE_READ,        /* sender requests data from receiver */
	SPI_TRANS_TYPE_WRITE,       /* sender provides data to receiver */
	SPI_TRANS_TYPE_REPLY,       /* reply from receiver */
	SPI_TRANS_TYPE_COUNT,
} Spi_TransType;

typedef enum
{
	SPI_DATA_TYPE_NONE = 0,
	SPI_DATA_TYPE_VEHICLE_SPEED,
	SPI_DATA_TYPE_COUNT,
} Spi_DataType;

typedef struct 
{
	int32_t    trans_type;
	int32_t    data_type;
} Spi_Header;


/* provide data */
int Spi_tx(void *data, uint32_t size, uint32_t flags)
{
	const uint32_t frame_size = sizeof(Spi_LinkFrame);
	Spi_Header header;
	Spi_LinkFrame link_frame;

	header.trans_type = SPI_TRANS_TYPE_WRITE;
	header.data_type = SPI_DATA_TYPE_NONE;

	/* 1. send the header first */
	assert(sizeof(header) <= sizeof(link_frame.payload));
	memcpy(&link_frame.payload, &header, sizeof(header));

	/* 2. send the payload of application data */

	if (size > frame_size) {
		/* split */
	}


}


/* request data */
int Spi_rx(void *data, uint32_t size, uint32_t flags)
{

}


//////////////////////////////////////////////////////////////////

/*
  link layer
  semantics: validity, re-send,
 */

typedef struct 
{
	byte_t        payload[32];
	uint8_t       check;
} Spi_LinkFrame;

int Spi_send_frame()
{

}

int Spi_recv_frame()
{

}


//////////////////////////////////////////////////////////////////

/* 
  physical layer
  semantics: handshake
 */

static int Spi_handshake()
{

}

int Spi_transfer()
{
	Spi_handshake();
}
